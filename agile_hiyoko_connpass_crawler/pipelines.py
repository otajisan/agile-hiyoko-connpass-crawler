import os
import sqlite3

from itemadapter import ItemAdapter


class AgileHiyokoConnpassCrawlerPipeline:
    _db = None

    @classmethod
    def get_database(cls):
        cls._db = sqlite3.connect(
            os.path.join(os.getcwd(), 'agile-hiyoko-connpass-crawler.db'))
        cursor = cls._db.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS connpass(\
                id INTEGER PRIMARY KEY AUTOINCREMENT, \
                event_id TEXT UNIQUE NOT NULL, \
                name TEXT UNIQUE NOT NULL, \
                url TEXT UNIQUE NOT NULL, \
                csv_url TEXT UNIQUE NOT NULL \
                );')

        return cls._db

    def process_item(self, entity, spider):
        if entity['name'] == '':
            return entity
        self.save(entity)
        return entity

    def save(self, entity):
        if self.find_by_url(entity['url']):
            return

        db = self.get_database()
        db.execute(
            'INSERT INTO connpass (event_id, name, url, csv_url) VALUES (?, ?, ?, ?)', (
                entity['event_id'],
                entity['name'],
                entity['url'],
                entity['csv_url']
            )
        )
        db.commit()

    def find_by_url(self, url):
        db = self.get_database()
        cursor = db.execute(
            'SELECT * FROM connpass WHERE url=?',
            (url,)
        )
        return cursor.fetchone()
