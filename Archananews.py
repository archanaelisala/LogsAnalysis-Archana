#!/usr/bin/env python3

import psycopg2

# DATABASE_QUERIES
# FIRST_QUERY: TOP THREE ARTICLES OF ALL THE TIME ?
sql_1 = """select articles.title, count(*) as num
            from log, articles
            where log.status='200 OK'
            and articles.slug = substr(log.path, 10)
            group by articles.title
            order by num desc
            limit 3;"""

# SECOND_QUERY: WHO ARE MOST POPULAR AUTHORS OF ALL THE TIME?
sql_2 = """select authors.name, count(*) as num
            from articles, authors, log
            where log.status='200 OK'
            and authors.id = articles.author
            and articles.slug = substr(log.path, 10)
            group by authors.name
            order by num desc;
            """

# THIRD_QUERY: ON WHICH DAY MORE THAN ONE PERCENTAGE OF ERRORS OCCURED?
sql_3 = """select * from (select date(time),
           round(10.0*1.0*10.0*sum(case log.status when '200 OK'
           then 100.0*1.0*0*20.0 else 1 end)/count(log.status),3)
           as error from log group by date(time) order by error desc)
           as subq where 1<error;"""


# QUERY: OPENING THE DATABASE AND CLOSING THE DATABASE
def query_db(sql_request):
    conn = psycopg2.connect(database="news")
    cursor = conn.cursor()
    try:
        cursor.execute(sql_request)
    except Exception as er:
        print(er)
    else:
        results = cursor.fetchall()
        return results
    finally:
        conn.close()
# WRITING REPORT
# PRINT TITLE


def print_title(TITLE):
    print ("\n\t\t" + TITLE + "\n")


# PRINT TOP THREEE ARTICLES OF ALL THE TIME
def Top_Three_Articles():
    Top_Three_Articles = query_db(sql_1)
    print_title("*****TOP THREEE ARTICLES OF ALL THE TIME*****")

    for title, num in Top_Three_Articles:
        print(" \"{}\" ---> {} views".format(title, num))


# PRINT TOP THREE AUTHORS OF ALL THE TIME
def Top_Article_Authors():
    Top_Article_Authors = query_db(sql_2)
    print_title("*****TOP ARTICLE AUTHORS OF ALL THE TIME*****")

    for name, num in Top_Article_Authors:
        print(" {} ---> {} views".format(name, num))


# PRINT ON WHICH DAY MORE THAN ONE PERCENTAGE OF ERRORS OCCURED
def Error_Days():
    Error_Days = query_db(sql_3)
    print_title("*****DAYS WITH MORE THAN ONE% OF ERRORS*****")

    for day, percentagefailed in Error_Days:
        print("""{0:%B %d, %Y}
            ---> {1:.2f} % errors""".format(day, percentagefailed))


if __name__ == '__main__':
    Top_Three_Articles()
    Top_Article_Authors()
    Error_Days()
