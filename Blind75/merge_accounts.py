from collections import defaultdict

def mergeAccounts(accounts):
    emailNames = {}
    graph = defaultdict(set)

    output = []

    # parse emails
    for account in accounts:
        name = account[0]
        firstEmail = account[1]
        emailNames[firstEmail] = name

        for followingEmail in account[2:]:
            graph[firstEmail].add(followingEmail)
            graph[followingEmail].add(firstEmail)
            emailNames[followingEmail] = name

    ans = []
    seenEmails = set()

    for email in emailNames:
        if email not in seenEmails:
            




    return graph



        

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

print(mergeAccounts(accounts))