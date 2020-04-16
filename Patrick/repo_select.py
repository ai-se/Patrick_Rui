import requests
import json
from time import sleep
import sys
from datetime import datetime

headers = {"Authorization": "token XXX"}


# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.
query1 = """
{
  viewer {
    login
  }
  rateLimit {
    limit
    cost
    remaining
    resetAt
  }
}
"""
query_limit = 1000

### settings
repoFirst=5
beginDate= "2015-01-01T00:00:00Z"
recentDate="2020-03-15T00:00:00Z"
recentIssues=1
recentPR=1
recentFork=1

subQueries_2015 = {"queryString":"is:public archived:false mirror:false created:2015-01-01..2016-01-01 stars:1000..10000 size:>=10000 forks:>=10",
                   "repoFirst": repoFirst,"beginDate":beginDate,"recentDate":recentDate,"recentIssues":recentIssues,"recentPR":recentPR,"recentFork":recentFork}
subQueries_2016 ={"queryString":"is:public archived:false mirror:false created:2016-01-01..2017-01-01 stars:1000..10000 size:>=10000 forks:>=10",
                   "repoFirst": repoFirst}#,"beginDate":beginDate,"recentDate":recentDate,"recentIssues":recentIssues,"recentPR":recentPR,"recentFork":recentFork}
subQueries_2017 = {"queryString":"is:public archived:false mirror:false created:2017-01-01..2018-01-01 stars:1000..10000 size:>=10000 forks:>=10",
                   "repoFirst": repoFirst}#,"beginDate":beginDate,"recentDate":recentDate,"recentIssues":recentIssues,"recentPR":recentPR,"recentFork":recentFork}
subQueries_2018 = {"queryString":"is:public archived:false mirror:false created:2018-01-01..2019-01-01 stars:1000..10000 size:>=10000 forks:>=10",
                   "repoFirst": repoFirst,"beginDate":beginDate,"recentDate":recentDate,"recentIssues":recentIssues,"recentPR":recentPR,"recentFork":recentFork}
subQueries_2019 = {"queryString":"is:public archived:false mirror:false created:2019-01-01..2020-01-01 stars:1000..10000 size:>=10000 forks:>=10",
                   "repoFirst": repoFirst,"beginDate":beginDate,"recentDate":recentDate,"recentIssues":recentIssues,"recentPR":recentPR,"recentFork":recentFork}
subQueries_2020 = {"queryString":"is:public archived:false mirror:false created:>=2020-01-01 stars:1000..10000 size:>=10000 forks:>=10",
                   "repoFirst": repoFirst,"beginDate":beginDate,"recentDate":recentDate,"recentIssues":recentIssues,"recentPR":recentPR,"recentFork":recentFork}


first_query="""
query{{
rateLimit {{
    remaining
    resetAt
}}
search(query:"{queryString}", type: REPOSITORY, first:{repoFirst}) {{
repositoryCount
pageInfo {{
  hasNextPage
  endCursor
}}
edges {{
  node {{
    ... on Repository {{
      id
      nameWithOwner
      description
      url
      stargazers {{
        totalCount
      }}
      watchers {{
        totalCount
      }}  # recent_watcher>1 not achievable
      forkCount
      recent_forks: forks(first: {recentFork}, orderBy: {{field: CREATED_AT, direction: DESC}}) {{
        edges {{
          node {{
            ... on Repository {{
              # id
              # nameWithOwner
              # description
              # url
              createdAt
            }}
          }}
        }}
      }}
      mergeCommitAllowed
      total_pr: pullRequests {{
        totalCount
      }}
      total_pr_closed: pullRequests(states: [CLOSED, MERGED]) {{
        totalCount
      }}
      recent_pr: pullRequests(first: {recentPR}, orderBy: {{field: CREATED_AT, direction: DESC}}) {{
        totalCount
        edges {{
          node {{
            ... on PullRequest {{
              # title
              # number
              # url
              # merged
              createdAt
            }}
          }}
        }}
      }}
      hasIssuesEnabled
      total_issues: issues {{
        totalCount
      }}
      total_issues_closed: issues(states: CLOSED) {{
        totalCount
      }}
      recent_issues: issues(first: {recentIssues}, orderBy: {{field: CREATED_AT, direction: DESC}}, filterBy: {{since: "{recentDate}"}}) {{
        totalCount
      }}
      assignableUsers {{
        totalCount
      }}
      defaultBranchRef {{
        name
        target {{
          ... on Commit {{
            # committer {{
            #   name
            #   email
            # }}
            recent_commit: history(since: "{recentDate}") {{
              totalCount
            }}
            total_commit: history(since: "{beginDate}"){{
              totalCount
            }}
          }}
        }}
      }}
    }}
  }}
}}
}}
}}
"""

following_query="""
query{{
rateLimit {{
    remaining
    resetAt
}}
search(query:"{queryString}", type: REPOSITORY, first:{repoFirst}, after:"{endCursor}") {{
repositoryCount
pageInfo {{
  hasNextPage
  endCursor
}}
edges {{
  node {{
    ... on Repository {{
      id
      nameWithOwner
      description
      url
      stargazers {{
        totalCount
      }}
      watchers {{
        totalCount
      }}  # recent_watcher>1 not achievable
      forkCount
      recent_forks: forks(first: {recentFork}, orderBy: {{field: CREATED_AT, direction: DESC}}) {{
        edges {{
          node {{
            ... on Repository {{
              # id
              # nameWithOwner
              # description
              # url
              createdAt
            }}
          }}
        }}
      }}
      mergeCommitAllowed
      total_pr: pullRequests {{
        totalCount
      }}
      total_pr_closed: pullRequests(states: [CLOSED, MERGED]) {{
        totalCount
      }}
      recent_pr: pullRequests(first: {recentPR}, orderBy: {{field: CREATED_AT, direction: DESC}}) {{
        totalCount
        edges {{
          node {{
            ... on PullRequest {{
              # title
              # number
              # url
              # merged
              createdAt
            }}
          }}
        }}
      }}
      hasIssuesEnabled
      total_issues: issues {{
        totalCount
      }}
      total_issues_closed: issues(states: CLOSED) {{
        totalCount
      }}
      recent_issues: issues(first: {recentIssues}, orderBy: {{field: CREATED_AT, direction: DESC}}, filterBy: {{since: "{recentDate}"}}) {{
        totalCount
      }}
      assignableUsers {{
        totalCount
      }}
      defaultBranchRef {{
        name
        target {{
          ... on Commit {{
            # committer {{
            #   name
            #   email
            # }}
            recent_commit: history(since: "{recentDate}") {{
              totalCount
            }}
            total_commit: history(since: "{beginDate}"){{
              totalCount
            }}
          }}
        }}
      }}
    }}
  }}
}}
}}
}}
"""
# In REST, HTTP verbs determine the operation performed. In GraphQL, you'll provide a JSON-encoded body whether you're performing a query or a mutation, so the HTTP verb is POST. The exception is an introspection query, which is a simple GET to the endpoint.
def run_query(query):  # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    #     print("request return code - {}".format(request.status_code))
    if request.status_code == 200:
        return request.json()
    else:
        tries=3
        while request.status_code != 200 and tries>0:
            print("sleep {} min".format(4-tries))
            sleep((4-tries)*60)

            request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
            tries-=1
            print("Retry {} th".format(3-tries))
        if request.status_code == 200:
            return request.json()
        else:
            print("request return code - {}".format(request.status_code))
            print(request.content)
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


def checkTokenLimit():
    result = run_query(query1)  # Execute the query
    remaining_rate_limit = result["data"]["rateLimit"]["remaining"]  # Drill down the dictionary
    print("Remaining rate limit - {}".format(remaining_rate_limit))

    resetTime = result["data"]["rateLimit"]["resetAt"]
    print("GitHub API must be reset to time - {}".format(resetTime))

    resetTime = datetime.strptime(resetTime, '%Y-%m-%dT%H:%M:%SZ')
    nowTimeUTC = datetime.utcnow()
    print("UTC time now - {}".format(nowTimeUTC))
    if nowTimeUTC.date() == resetTime.date() and nowTimeUTC.time() < resetTime.time():
        print("will reset in future")
        return remaining_rate_limit
    else:
        raise Exception("resetAt error")

def getFirstQuerySearch(variables):
    return first_query.format(**variables)

def getFollowingQuerySearch(variables,endCursor):
    variables["endCursor"] = endCursor
    return following_query.format(**variables)

def getRepoUrls(subquery):
    query=getFirstQuerySearch(subquery)
    # print(query)
    result = run_query(query)
    print(result['data']['search']['repositoryCount'])
    data=result['data']['search']["edges"]
    lastCursor = result['data']['search']['pageInfo']['endCursor']
    hasNextPage = result['data']['search']['pageInfo']['hasNextPage']
    for info in data:
        repo=info['node']
        print(repo["url"])
    print(lastCursor)
    count=1
    while hasNextPage:
        query=getFollowingQuerySearch(subquery,endCursor=lastCursor)
        result = run_query(query)
        if "errors" in result:
            print(query)
            print(result)
            raise Exception("error in processing query: "+subquery+" iteration: "+str(count))
        data = result['data']['search']["edges"]
        lastCursor = result['data']['search']['pageInfo']['endCursor']
        hasNextPage = result['data']['search']['pageInfo']['hasNextPage']
        for info in data:
            repo = info['node']
            print(repo["url"])
        print(lastCursor)
        remain_token = result["data"]["rateLimit"]["remaining"]
        print("remain token - {}".format(remain_token))

        if remain_token<5:
            sleep(3600)
            while checkTokenLimit() < 4000:
                sleep(60)
        count+=1


def checkTokenLimit():
    result = run_query(query1)  # Execute the query
    remaining_rate_limit = result["data"]["rateLimit"]["remaining"]  # Drill down the dictionary
    print("Remaining rate limit - {}".format(remaining_rate_limit))

    resetTime = result["data"]["rateLimit"]["resetAt"]
    print("GitHub API must be reset to time - {}".format(resetTime))

    resetTime = datetime.strptime(resetTime, '%Y-%m-%dT%H:%M:%SZ')
    nowTimeUTC = datetime.utcnow()
    print("UTC time now - {}".format(nowTimeUTC))
    if nowTimeUTC.date() == resetTime.date() and nowTimeUTC.time() < resetTime.time():
        print("will reset in future")
        return remaining_rate_limit
    else:
        raise Exception("resetAt error")

if __name__ == '__main__':
    #     checkTokenLimit()
    getRepoUrls(subQueries_2015)
    # lists=[subQueries_2015,subQueries_2016,subQueries_2017,subQueries_2018,subQueries_2019,subQueries_2020]
    # for subquery in lists:
    #     getRepoUrls(subquery)
