from G8RNG import XOROSHIRO,Raid
seed = 0x03E4BC1CC8FD6C5F
ivfilter = 1
Maxresults = 2000
V6 = [31,31,31,31,31,31]
S0 = [31,31,31,31,31,00]
A0 = [31,00,31,31,31,31]
 
# Main
i = 0
while i < Maxresults:
    r = Raid(seed, flawlessiv = 4, HA = 1, RandomGender = 1)
    seed = XOROSHIRO(seed).next()
    if ivfilter:
        if r.ShinyType != 'None' or r.IVs == V6 or r.IVs == S0 or r.IVs == A0:
            print(i)
            r.print()
    else:
        r.print()
    i += 1