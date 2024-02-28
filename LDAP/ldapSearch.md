# Reprend les infos du serveur 
    ldapsearch -H ldap://localhost:389 -x -D "cn=admin,dc=mydomain,dc=local" -w ranma -b "dc=mydomain,dc=local"
    