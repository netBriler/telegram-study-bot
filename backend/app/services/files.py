from app.models import File

from typing import List


def get_file(id: int) -> File:
    file = File.query.filter_by(id=id).first()
    return file


def get_all_files() -> List[File]:
    files = File.query.all()
    return files

