from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run Playwright E2E tests with shared CI settings.")
    parser.add_argument(
        "--target",
        default="tests/e2e/test_parabank.py",
        help="Pytest target to execute.",
    )
    parser.add_argument(
        "--report-dir",
        default="artifacts/reports",
        help="Directory for HTML and JUnit reports.",
    )
    parser.add_argument(
        "--screenshot-dir",
        default="artifacts/screenshots",
        help="Directory for failure screenshots.",
    )
    parser.add_argument(
        "--html-report",
        default="pytest-report.html",
        help="HTML report filename inside the report directory.",
    )
    parser.add_argument(
        "--junit-report",
        default="junit.xml",
        help="JUnit XML filename inside the report directory.",
    )
    parser.add_argument(
        "--tb",
        default="short",
        help="Pytest traceback style.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    project_root = Path.cwd()
    report_dir = Path(args.report_dir)
    screenshot_dir = Path(args.screenshot_dir)
    report_dir.mkdir(parents=True, exist_ok=True)
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(project_root)

    command = [
        sys.executable,
        "-m",
        "pytest",
        args.target,
        f"--html={report_dir / args.html_report}",
        "--self-contained-html",
        f"--junitxml={report_dir / args.junit_report}",
        f"--tb={args.tb}",
    ]

    return subprocess.call(command, env=environment)


if __name__ == "__main__":
    raise SystemExit(main())
