#!/usr/bin/env python2

import psycopg2

PopularTitle = 'What are the most popular three articles of all time?'
PopularQuery = """
SELECT title, count(*) as num FROM articles, log
      WHERE articles.slug = substring(log.path, 10)
      GROUP BY title ORDER BY num DESC LIMIT 3;
"""
MostTitle = 'Who are the most popular article authors of all time?'
MostQuery = """
SELECT authors.name, count(*) AS num
      FROM articles
      JOIN authors on articles.author = authors.id
      JOIN log on articles.slug = substring(log.path, 10)
      WHERE log.status LIKE '200 OK'
      GROUP BY authors.name ORDER BY num desc;
"""

ErrorTitle = 'On which days did more than 1% of requests lead to errors?'
ErrorQuery = """
SELECT * FROM (
    SELECT m.day,
    round(cast((100*n.click) as numeric) / cast(m.click as numeric), 2)
    as ep FROM
        (SELECT date(time) as day, count(*) as click FROM log
        GROUP BY day) as m
        JOINs
        (SELECT date(time) as day, count(*) as click FROM log
        WHERE status
        LIKE '%NOT FOUND%' GROUP BY day) as n
    on m.day = n.day)
as f WHERE ep > 1.0;
"""


class Queires:
    def __init__(self):
        try:
            self.db = psycopg2.connect('dbname=news')
            self.cursor = self.db.cursor()
        except Exception as ex:
            print ex

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def Q(self, title, query, cshow='views'):
        query = query.replace('\n', ' ')
        result = self.execute_query(query)
        print title
        for i in range(len(result)):
            print '\t', i + 1, '.', result[i][0], '--', result[i][1], cshow

        print ''

    def exit(self):
        self.db.close()


if __name__ == '__main__':
    Queires = Queires()
    Queires.Q(PopularTitle, PopularQuery)
    Queires.Q(MostTitle, MostQuery)
    Queires.Q(ErrorTitle, ErrorQuery, '% error')
    Queires.exit()
