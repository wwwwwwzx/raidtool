from G8RNG import XOROSHIRO,Raid

PID = 0x9c86F7F8
EC = 0x9dffc477
IVs = [14,31,31,31,10,24]
usefilters = True
MaxResults = 500

# Desired IVs
V6 = [31,31,31,31,31,31]
S0 = [31,31,31,31,31,00]
A0 = [31,00,31,31,31,31]

# Find seeds
results = Raid.getseeds(EC,PID,IVs)

if len(results) == 0:
    print("No raid seed")
else:  
    for result in results:
        if result[1] > 0:
            print(f"seed = 0x{result[0]:016X}\nPerfect IVs:{result[1]}")
            r = Raid(result[0],flawlessiv = result[1], HA = 0, RandomGender = 0)
            r.print()
        else:
            print(f"seed = 0x{result[0]:016X}\n(Shiny locked!) Perfect IVs:{-result[1]}")
            r = Raid(result[0],flawlessiv = -result[1], HA = 1, RandomGender = 0)
            r.print()

# Calc frames
if len(results) > 0:
	print(f"\n\nResults:")
	seed = results[0][0]
	i = 0
	while i < MaxResults:
		r = Raid(seed, flawlessiv = 4, HA = 1, RandomGender = 0)
		seed = XOROSHIRO(seed).next()
		if usefilters:
			if r.ShinyType != 'None' or r.IVs == V6 or r.IVs == S0 or r.IVs == A0:
				print(i)
				r.print()
		else:
			r.print()
		i += 1

