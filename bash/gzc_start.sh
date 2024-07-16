#!/bin/bash  
  
PROJECT_DIR="/home/ai-work/GzcAI"  
GZCAI_DIR="${PROJECT_DIR}/gzcai"  
WEBSITE_DIR="${PROJECT_DIR}/web"  
  

cd "$GZCAI_DIR" || exit  
  

uvicorn server:app --host 0.0.0.0 --port 8888 & 

sleep 3
  
cd "$WEBSITE_DIR" || exit  
npm run dev  
  

