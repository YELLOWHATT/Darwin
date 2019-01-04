import sqlite3

conn = sqlite3.connect('bob_bacteria.db')

cur = conn.cursor()

# allbacterias = []
#
# bac00000001 = ["Eschericia Coli", "Gram Negative", "Coli", "Shiga Toxin"] # 1
# bac00000011 = ["Pseudomonas Aeruginosa", "Gram Negatove", "Aeruginosa", "Lorem ipsum"] # 3
# bac00000101 = ["Salmonella Enterica", "Gram Negative", "Enterica", "Lorem  ipsum"] # 5
# bac00000111 = ["Helicobacter Pylori", "Gram Negative", "Pylori", "Stomach Ulcers"] # 7
# bac00001001 = ["Klebsiella Pneumoniae", "Gram Negative", "Pneumoniae", "Lorem ipsum"] # 9
#
# allbacterias.append(bac00000001)
# allbacterias.append(bac00000011)
# allbacterias.append(bac00000101)
# allbacterias.append(bac00000111)
# allbacterias.append(bac00001001)
#
# for bacteria in allbacterias:
#     cur.execute("SELECT * FROM bob WHERE name=?", (bacteria[0],))
#     exists = cur.fetchone()
#     if not exists and bacteria[3]:
#         cur.execute("INSERT into bob VALUES (?, ?, ?, ?)", bacteria)
#     if not exists and not bacteria[3]:
#         cur.execute("INSERT into bob VALUES (?, ?, ?)", bacteria)
#     else:
#         print("Bob alredy in the database")

cur.execute("INSERT into bob VALUES (?, ?, ?, null)", ("lol", "xd", "ok"))
conn.commit()
cur.close()
conn.close()

