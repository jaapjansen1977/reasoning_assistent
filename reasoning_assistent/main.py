"""Klein startpunt; samenstelling en UI zitten in aparte modules."""
import argparse
from .bootstrap import build_service
from .demo import DEMO_TRANSCRIPT


def main() -> None:
    parser = argparse.ArgumentParser(description="Modulaire consultassistent (demo)")
    parser.add_argument("--demo", action="store_true", help="Tekstdemo zonder venster")
    args = parser.parse_args()
    service = build_service()
    if args.demo:
        for item in service.analyze(DEMO_TRANSCRIPT).suggestions:
            print(f"[DEMO] {item.question}\n{item.reason}\n")
    else:
        from .ui.desktop import launch
        launch(service)
