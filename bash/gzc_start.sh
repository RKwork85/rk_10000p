#!/bin/bash

PROJECT_DIR="/home/ai-work/GzcAI"
GZCAI_DIR="${PROJECT_DIR}/gzcai"
WEBSITE_DIR="${PROJECT_DIR}/web"

# 启动 FastAPI 应用
cd "$GZCAI_DIR" || exit
uvicorn server:app --host 0.0.0.0 --port 8888 &

# 等待 FastAPI 应用启动
sleep 3

# 启动前端开发服务器
cd "$WEBSITE_DIR" || exit
npm run dev &