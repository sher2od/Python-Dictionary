usesr = [
    {
        "name":"Sherzod",
        "age":19
    },

    {
        "name":"ozod",
        "age":20
        
    },

    {
        "name":"sobir",
        "age":22
    },

    {
        "name":"ali",
        "age":20
    },

    {
        "name":"Sherzod",
        "age":20
    }
    
    ]

oldest_user = usesr[0]

for user in usesr:
    if user['age'] > oldest_user['age']:
        oldest_user = user

print(oldest_user)


















