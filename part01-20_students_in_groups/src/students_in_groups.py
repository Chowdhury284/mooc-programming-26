student= int(input("How many students on the course? "))
groupe= int(input("Desired group size? "))
dived= (student+groupe-1)// groupe
print(f"Number of groups formed: {dived}")