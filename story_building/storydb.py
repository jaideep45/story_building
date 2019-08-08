from story import Story, Paragraph, Sentence
import MySQLdb
import json
from flask.json import jsonify
import story

class StoryDB:
    con = MySQLdb.connect(host = "localhost",user = "root", passwd = "mysql@123",db ="api", use_unicode=True, charset="utf8")
    con.autocommit(True)
    
    def pop_story(self):
        cursor = self.con.cursor()
        query = "select * from stories_all where is_full <> 1 order by updated_at desc, created_at desc limit 1"
        cursor.execute(query)
        contents = cursor.fetchone()
        str = Story(id=contents[0],created_at=contents[4],updated_at=contents[5],content = json.loads(contents[2]))
        return str
        
    def update(self,story):
        if id is not None:
            cursor = self.con.cursor()
            query = "update stories_all set story_content = %s ,is_full= %s where id  = %s"
            cursor.execute(query,(json.dumps(story.compose_array()),story.is_full,story.id))
        
    def upload(self,story):
        cursor = self.con.cursor()
        if story.id is None:
            query ="insert into stories_all(title,story_content,is_full) values(%s,%s,%s)"
            cursor.execute(query,(story.compose_title(),json.dumps(story.compose_array()),story.is_full))
            
    def fetch_stories(self,limit,offset):
        cursor = self.con.cursor()
        query = "select * from stories-all order by updated_at desc limit %s %s"
        cursor.execute(query,(offset,limit))
        results = cursor.fetchall()
        stories = []
        for result in results:
            story = Story(id=result[0],created_at=result[4],updated_at=result[5],content = json.loads(result[2]))
            stories.append(story)
        return stories
    
    
 
    