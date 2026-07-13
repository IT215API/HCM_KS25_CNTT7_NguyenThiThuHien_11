from sqlalchemy.orm import Session
from models import MeetingModel
from schemas import MeetingRequestDTO
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

# lấy danh sách phòng họp
def get_all(db: Session):
    data_room = db.query(MeetingModel).all()
    return data_room

# tìm phòng họp theo trạng thái
def get_room_status(db: Session, status: str):
    data_room = db.query(MeetingModel).filter(MeetingModel.status.like(f"{status}")).all()
    if data_room is None:
        raise HTTPException(status_code=404, detail="Not found")
    return data_room

# lấy chi tiết phòng họp
def get_room_by_id(db: Session, room_id: int):
    data_room = db.query(MeetingModel).filter(MeetingModel.id == room_id).first()
    if data_room is None:
        raise HTTPException(status_code=404, detail="Not found")
    return data_room

# thêm phòng họp
def create_room(db: Session, meeting_room=MeetingRequestDTO):
    try:
        new_room = MeetingModel(
            room_name = meeting_room.room_name,
            floor = meeting_room.floor,
            capacity = meeting_room.capacity,
            status = meeting_room.status
        )
        db.add(new_room)
        db.commit()
        db.refresh(new_room)
        return new_room
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Lỗi database không xác định"
        )

# cập nhật phòng họp
def update_room(db: Session, room_id: int, room: MeetingRequestDTO):
    try:
        find_room = get_room_by_id(db, room_id)
        find_room.room_name = room.room_name
        find_room.floor = room.floor
        find_room.capacity = room.capacity
        find_room.status = room.status
        db.commit()
        db.refresh(find_room)
        return find_room
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Lỗi database không xác định"
        )
    
# xóa phòng họp
def delete_room(db: Session, room_id: int):
    find_room = get_room_by_id(db, room_id)
    if find_room is None:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(find_room)
    db.commit()
    return find_room