from fastapi import FastAPI, Depends, status, HTTPException
from database import Base, engine, get_db
from models import MeetingModel
from schemas import notice_api, MeetingRequestDTO
import meeting_services as ms
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

# API kiểm tra server
@app.get("/")
def get_test():
    return {
        "message": "API đang chạy",
        "data": None
    }

# API lấy danh sách phòng họp
@app.get("/meeting-rooms", tags=["Meeting Rooms"], status_code=status.HTTP_200_OK)
def get_all(db: Session = Depends(get_db)):
    data_meeting = ms.get_all(db)
    return notice_api(
        200,
        None,
        "Lấy thành công",
        data_meeting
    )

# API tìm kiếm phòng họp theo status
@app.get("/meeting-rooms/status", tags=["Meeting Rooms"], status_code=status.HTTP_200_OK)
def get_room_status(status: str, db: Session = Depends(get_db)):
    data_meeting = ms.get_room_status(db, status)
    return notice_api(
        200,
        None,
        "Lấy thành công",
        data_meeting
    )

# API lấy chi tiết phòng họp
@app.get("/meeting-rooms/{room_id}", tags=["Meeting Rooms"], status_code=status.HTTP_200_OK)
def get_room_id(room_id: int, db: Session = Depends(get_db)):
    data_meeting = ms.get_room_by_id(db, room_id)
    # return {
    #     "statusCode": 200,
    #     "data": data_meeting,
    #     "message": "Lấy thành công"
    # }
    return notice_api(
        200,
        None,
        "Lấy thành công",
        data_meeting
    )

# API thêm phòng họp
@app.post("/meeting-rooms/{room_id}", tags=["Meeting Rooms"], status_code=status.HTTP_201_CREATED)
def create_room(meeting_room: MeetingRequestDTO, db: Session = Depends(get_db)):
    data_meeting = ms.create_room(db, meeting_room)
    return notice_api(
        201,
        None,
        "Thêm thành công",
        data_meeting
    )

# API cập nhật phòng họp
@app.put("/meeting-rooms/{room_id}", tags=["Meeting Rooms"], status_code=status.HTTP_200_OK)
def update_room(room_id: int, meeting_room: MeetingRequestDTO, db: Session = Depends(get_db)):
    data_meeting = ms.update_room(db, room_id, meeting_room)
    return notice_api(
        200,
        None,
        "Cập nhật thành công",
        data_meeting
    )

# API xóa phòng họp
@app.delete("/meeting-rooms/{room_id}", tags=["Meeting Rooms"], status_code=status.HTTP_200_OK)
def delete_room(room_id: int, db: Session = Depends(get_db)):
    data_meeting = ms.delete_room(db, room_id)
    return notice_api(
        200,
        None,
        "Xóa thành công",
        data_meeting
    )
