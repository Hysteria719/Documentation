# Reprend les infos du serveur 
    ldapsearch -H ldap://localhost:389 -x -D "cn=admin,dc=mydomain,dc=local" -w ranma -b "dc=mydomain,dc=local"

# Lien
    https://docs.oracle.com/cd/E19623-01/820-6169/ldapsearch-examples.html
