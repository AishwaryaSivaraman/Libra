
# < 25
assume(0 <= x02 <= 0)
assume(1 <= x03 <= 1)
assume(0 <= x04 <= 0)

x10 = (0.318898)*x00 + (-0.478490)*x01 + (-0.268742)*x02 + (0.129693)*x03 + (0.239745)*x04 + (-0.120753)*x05 + (0.336760)*x06 + (-0.241058)*x07 + (0.224208)*x08 + (-0.122410)*x09 + (0.178727)*x010 + (0.790230)*x011 + (0.319575)*x012 + (0.009091)*x013 + (0.372656)*x014 + (-0.435531)*x015 + (-0.308371)*x016 + (-0.447535)*x017 + (0.121315)*x018 + (-0.071339)
x11 = (0.550245)*x00 + (0.280048)*x01 + (0.303227)*x02 + (0.187561)*x03 + (-0.348396)*x04 + (-0.136309)*x05 + (-0.182506)*x06 + (-0.115206)*x07 + (-0.063355)*x08 + (-0.085800)*x09 + (-0.142046)*x010 + (0.776769)*x011 + (1.009998)*x012 + (0.014174)*x013 + (-0.224876)*x014 + (0.100403)*x015 + (0.289661)*x016 + (-0.316188)*x017 + (0.168260)*x018 + (0.121363)
x12 = (0.017920)*x00 + (-0.484051)*x01 + (-0.007149)*x02 + (0.147824)*x03 + (-0.401516)*x04 + (0.098991)*x05 + (-0.289692)*x06 + (0.155018)*x07 + (0.262889)*x08 + (0.327689)*x09 + (0.170729)*x010 + (0.148915)*x011 + (-0.201399)*x012 + (0.177076)*x013 + (0.271014)*x014 + (-0.135306)*x015 + (0.415253)*x016 + (-0.464619)*x017 + (0.464201)*x018 + (-0.005861)
x13 = (0.014808)*x00 + (0.279372)*x01 + (-0.127246)*x02 + (0.425626)*x03 + (0.486702)*x04 + (0.101052)*x05 + (0.204817)*x06 + (0.107354)*x07 + (0.044787)*x08 + (0.119320)*x09 + (0.156190)*x010 + (1.217197)*x011 + (1.304542)*x012 + (-0.239425)*x013 + (-0.014949)*x014 + (0.028464)*x015 + (-0.133514)*x016 + (-0.164843)*x017 + (-0.226389)*x018 + (0.098606)
x14 = (0.006781)*x00 + (-0.002445)*x01 + (-0.396703)*x02 + (0.058303)*x03 + (-0.038767)*x04 + (0.215432)*x05 + (0.176309)*x06 + (-0.029883)*x07 + (-0.469178)*x08 + (0.350289)*x09 + (-0.030513)*x010 + (0.293366)*x011 + (0.257355)*x012 + (-0.117298)*x013 + (0.020605)*x014 + (-0.341880)*x015 + (0.328173)*x016 + (-0.471549)*x017 + (0.456380)*x018 + (0.092141)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (-0.493118)*x10 + (0.203431)*x11 + (-0.016635)*x12 + (0.742006)*x13 + (-0.164663)*x14 + (-0.100741)
x21 = (-0.294618)*x10 + (0.617842)*x11 + (-0.433102)*x12 + (0.001834)*x13 + (-0.002371)*x14 + (-0.042919)
x22 = (-0.754742)*x10 + (-0.807590)*x11 + (-0.839531)*x12 + (0.589022)*x13 + (-0.525656)*x14 + (0.152529)
x23 = (0.463200)*x10 + (-0.513375)*x11 + (-0.564590)*x12 + (0.647277)*x13 + (0.688317)*x14 + (-0.009797)
x24 = (-0.038711)*x10 + (0.767932)*x11 + (-0.139445)*x12 + (0.870897)*x13 + (0.015053)*x14 + (-0.090179)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (0.032226)*x20 + (0.395558)*x21 + (0.374455)*x22 + (-0.513740)*x23 + (0.473444)*x24 + (0.148338)
x31 = (0.229822)*x20 + (0.245428)*x21 + (-0.740051)*x22 + (0.214946)*x23 + (0.599252)*x24 + (-0.080365)
x32 = (0.721349)*x20 + (-0.028996)*x21 + (-0.300659)*x22 + (-0.180713)*x23 + (0.686058)*x24 + (-0.158217)
x33 = (-0.108674)*x20 + (-0.778809)*x21 + (0.389751)*x22 + (0.219606)*x23 + (0.357877)*x24 + (0.132762)
x34 = (0.385866)*x20 + (0.479243)*x21 + (-0.094022)*x22 + (-0.742838)*x23 + (-0.400006)*x24 + (-0.047070)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (-0.605646)*x30 + (0.162936)*x31 + (0.304437)*x32 + (0.879623)*x33 + (0.527090)*x34 + (0.059002)
x41 = (0.555051)*x30 + (-0.053867)*x31 + (-0.538083)*x32 + (-0.776977)*x33 + (0.505254)*x34 + (0.062006)
x42 = (-0.984404)*x30 + (0.297861)*x31 + (0.377710)*x32 + (-0.484443)*x33 + (-0.022561)*x34 + (-0.264141)
x43 = (0.528027)*x30 + (0.672076)*x31 + (1.160404)*x32 + (-0.435967)*x33 + (-0.707740)*x34 + (-0.092493)
x44 = (0.443926)*x30 + (-0.183157)*x31 + (-0.770593)*x32 + (0.518208)*x33 + (0.275581)*x34 + (0.357435)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (-0.333180)*x40 + (-0.450527)*x41 + (0.508127)*x42 + (-1.233798)*x43 + (0.372009)*x44 + (0.093539)
x51 = (0.426619)*x40 + (0.553823)*x41 + (0.280644)*x42 + (-0.404479)*x43 + (-0.423400)*x44 + (-0.020596)
x52 = (-0.686171)*x40 + (-1.166686)*x41 + (0.371507)*x42 + (0.358985)*x43 + (-0.911725)*x44 + (-0.055146)
#
