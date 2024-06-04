import datetime
from fastapi import FastAPI, WebSocket, Request
from fastapi.templating import Jinja2Templates
import cv2
import concurrent.futures
from database.database import create_db_if_not_exists, add_data
import base64
import multiprocessing

app = FastAPI()
templates = Jinja2Templates(directory="templates")
camera = cv2.VideoCapture(0)

create_db_if_not_exists()

@app.get("/")
async def get(req: Request):
    return templates.TemplateResponse(
        request=req, name="index.html")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    while True:
        data = await websocket.receive_json()
        
        if data["event"] == "mousemove":
            await websocket.send_text(f"Current_position: x:{data["x"]}, y:{data["y"]} ")
            
        if data["event"] == "mouseup":
            x_pos = data["x"]
            y_pos = data["y"]
            
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            process = multiprocessing.Process(target=take_picture_and_save, args=(timestamp,x_pos,y_pos))
            process.run()

def take_picture_and_save(timestamp, x, y):
    _, frame = camera.read()
    _, buffer = cv2.imencode('.jpg', frame)
    img_str = base64.b64encode(buffer).decode('utf-8')
    
    add_data(timestamp, x, y, img_str)
    