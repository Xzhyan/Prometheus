@echo off
@chcp 65001 > nul
title Prometheus CLI Tool

.venv\Scripts\activate && python -m src.main
