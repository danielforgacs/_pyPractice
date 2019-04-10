"""
modify a line to make this work.
"""

c = ['Alpha', 'Beta', 'Gamma']

for k in c:
    type(k, (object,), {k: 1})

print Alpha.Alpha
print Beta.Beta
print Gamma.Gamma
