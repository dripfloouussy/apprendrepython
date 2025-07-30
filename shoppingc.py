#Exercice 2 shopping cart prgram

article= input("Quel article voulez vous achetez?:")
prix = float(input("Quel est le prix:"))
quantite = int(input("combien voulez vous?:"))
total = prix * quantite
print((f"tu as un budget{quantite} x {article}/s"))

print(f"ton total est : {total}")

#print(total)