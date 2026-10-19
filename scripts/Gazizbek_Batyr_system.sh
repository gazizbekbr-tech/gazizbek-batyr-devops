#!/usr/bin/env bash
# System information script for Batyr Gazizbek

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
INFO_FILE="$SCRIPT_DIR/../Gazizbek_Batyr_info.txt"

echo "=============================="
echo "Student Information"
echo "=============================="
echo
echo "Name: Batyr"
echo "Surname: Gazizbek"
echo "Group: IT2-2301"
echo "Student ID: 38091"
echo
echo "=============================="
echo "System Information"
echo "=============================="
echo
echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current Date: $(date)"
echo "Operating System: $(uname -sr)"
echo "Disk Usage:"
df -h / | tail -n +1
echo "Memory Usage:"
if command -v free >/dev/null; then free -h; else vm_stat | head -5; fi
echo

if [ -f "$INFO_FILE" ]; then
  echo "Student information file exists."
else
  echo "Student information file does not exist."
fi
