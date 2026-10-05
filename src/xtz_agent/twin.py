import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from .config import settings

SCHEMA = """
CREATE TABLE IF NOT EXISTS measurements(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created_at TEXT NOT NULL,
  target TEXT NOT NULL,
  value REAL NOT NULL,
  unit TEXT NOT NULL,
  method TEXT NOT NULL,
  uncertainty TEXT,
  status TEXT NOT NULL DEFAULT 'BIKE_CONFIRMED'
);
CREATE TABLE IF NOT EXISTS service_events(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created_at TEXT NOT NULL,
  odometer_km REAL,
  system TEXT NOT NULL,
  action TEXT NOT NULL,
  parts_json TEXT NOT NULL DEFAULT '[]',
  notes TEXT
);
CREATE TABLE IF NOT EXISTS observations(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created_at TEXT NOT NULL,
  system TEXT NOT NULL,
  finding TEXT NOT NULL,
  status TEXT NOT NULL,
  source TEXT
);
"""

class DigitalTwinStore:
    def __init__(self, db_path: Path | None = None):
        self.db_path = Path(db_path or settings.twin_db)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as con:
            con.executescript(SCHEMA)

    def _connect(self):
        con = sqlite3.connect(self.db_path)
        con.row_factory = sqlite3.Row
        return con

    @staticmethod
    def _now():
        return datetime.now(timezone.utc).isoformat()

    def add_measurement(self, target, value, unit, method, uncertainty=None, status="BIKE_CONFIRMED"):
        with self._connect() as con:
            cur = con.execute(
                "INSERT INTO measurements(created_at,target,value,unit,method,uncertainty,status) VALUES(?,?,?,?,?,?,?)",
                (self._now(), target, value, unit, method, uncertainty, status),
            )
            row = con.execute("SELECT * FROM measurements WHERE id=?", (cur.lastrowid,)).fetchone()
            return dict(row)

    def add_service_event(self, system, action, odometer_km=None, parts=None, notes=None):
        with self._connect() as con:
            cur = con.execute(
                "INSERT INTO service_events(created_at,odometer_km,system,action,parts_json,notes) VALUES(?,?,?,?,?,?)",
                (self._now(), odometer_km, system, action, json.dumps(parts or [], ensure_ascii=False), notes),
            )
            row = con.execute("SELECT * FROM service_events WHERE id=?", (cur.lastrowid,)).fetchone()
            result = dict(row)
            result["parts"] = json.loads(result.pop("parts_json"))
            return result

    def add_observation(self, system, finding, status, source=None):
        with self._connect() as con:
            cur = con.execute(
                "INSERT INTO observations(created_at,system,finding,status,source) VALUES(?,?,?,?,?)",
                (self._now(), system, finding, status, source),
            )
            row = con.execute("SELECT * FROM observations WHERE id=?", (cur.lastrowid,)).fetchone()
            return dict(row)

    def snapshot(self):
        with self._connect() as con:
            measurements = [dict(r) for r in con.execute("SELECT * FROM measurements ORDER BY id DESC LIMIT 200")]
            observations = [dict(r) for r in con.execute("SELECT * FROM observations ORDER BY id DESC LIMIT 200")]
            events = []
            for r in con.execute("SELECT * FROM service_events ORDER BY id DESC LIMIT 200"):
                row = dict(r)
                row["parts"] = json.loads(row.pop("parts_json"))
                events.append(row)
        return {"measurements":measurements,"observations":observations,"service_events":events}
