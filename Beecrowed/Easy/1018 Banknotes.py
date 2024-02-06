value = int(input() )
print(value)
value , hundred =value%100, value//100 
value , fifty =value%50, value//50

value , twenty =value%20, value//20

value , ten =value%10, value//10

value , five = value % 5, value //5
value , two = value % 2, value //2
value , one = value % 1, value //1

print(f'''{hundred} nota(s) de R$ 100,00
{fifty} nota(s) de R$ 50,00
{twenty} nota(s) de R$ 20,00
{ten} nota(s) de R$ 10,00
{five} nota(s) de R$ 5,00
{two} nota(s) de R$ 2,00
{one} nota(s) de R$ 1,00''')

