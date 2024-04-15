cookie = """
i=z1PQa5TmbOAKoCV1YpHcsvGEmy+FLow0N4PSjS+FGcQZcLJMR7WJbAJaPkxCEHSVVlYTJHkduEBmWr9hQDO6c3lwcx4=; yandexuid=5478701451693998810; yabs-sid=443727641698054835; yuidss=5478701451693998810; ymex=2017031292.yrts.1701671292#2009358810.yrtsi.1693998810; yashr=2012744691712217271; bh=EkAiR29vZ2xlIENocm9tZSI7dj0iMTIzIiwgIk5vdDpBLUJyYW5kIjt2PSI4IiwgIkNocm9taXVtIjt2PSIxMjMiGgUiYXJtIiIQIjExOS4wLjYwNDUuMTk5IioCPzAyCSJOZXh1cyA1IjoHIm1hY09TIkIIIjE0LjEuMCJKBCI2NCJSXCJHb29nbGUgQ2hyb21lIjt2PSIxMTkuMC42MDQ1LjE5OSIsIkNocm9taXVtIjt2PSIxMTkuMC42MDQ1LjE5OSIsIk5vdD9BX0JyYW5kIjt2PSIyNC4wLjAuMCIi; receive-cookie-deprecation=1; bh=Ej4iR29vZ2xlIENocm9tZSI7dj0iMTIzIiwiTm90OkEtQnJhbmQiO3Y9IjgiLCJDaHJvbWl1bSI7dj0iMTIzIhoFImFybSIiECIxMjMuMC42MzEyLjEyMiIqAj8wMgkiTmV4dXMgNSI6ByJtYWNPUyJCCCIxNC40LjEiSgQiNjQiUlsiR29vZ2xlIENocm9tZSI7dj0iMTIzLjAuNjMxMi4xMjIiLCJOb3Q6QS1CcmFuZCI7dj0iOC4wLjAuMCIsIkNocm9taXVtIjt2PSIxMjMuMC42MzEyLjEyMiIi"""





cookies = cookie.split(";")

dicts = {}
for i in cookies:
    strs = i.split("=",1)
    print("\"{0}\"".format(strs[0]),":\"{0}\"".format(strs[1]))
    # dicts.update({strs[0],strs[1]})
