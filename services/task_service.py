from datetime import datetime
from app import db
from app.models.task import Task

class TaskService:
    @staticmethod
    def create(data):
        task = Task(
            title=data["title"],
            description=data["description"],
            status=data.get("status", "new")
        )
        db.session.add(task)
        db.session.commit()
        return task

    @staticmethod
    def get_all(page=1, limit=10):
        query = Task.query.filter(Task.deleted_at.is_(None))
        total = query.count()

        tasks = (
            query.order_by(Task.created_at.desc())
            .offset((page - 1) * limit)
            .limit(limit)
            .all()
        )

        return {
            "data": [task.to_dict() for task in tasks],
            "meta": {
                "total": total,
                "page": page,
                "limit": limit,
                "totalPages": (total + limit - 1) // limit
            }
        }

    @staticmethod
    def get_one(task_id):
        return Task.query.filter_by(id=task_id, deleted_at=None).first()

    @staticmethod
    def update_put(task_id, data):
        task = Task.query.filter_by(id=task_id, deleted_at=None).first()
        if not task:
            return None

        task.title = data["title"]
        task.description = data["description"]
        task.status = data["status"]
        db.session.commit()
        return task

    @staticmethod
    def update_patch(task_id, data):
        task = Task.query.filter_by(id=task_id, deleted_at=None).first()
        if not task:
            return None

        if "title" in data:
            task.title = data["title"]
        if "description" in data:
            task.description = data["description"]
        if "status" in data:
            task.status = data["status"]

        db.session.commit()
        return task

    @staticmethod
    def soft_delete(task_id):
        task = Task.query.filter_by(id=task_id, deleted_at=None).first()
        if not task:
            return None

        task.deleted_at = datetime.utcnow()
        db.session.commit()
        return task