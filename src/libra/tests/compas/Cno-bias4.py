
# caucasian
assume(0 <= x05 <= 0)
assume(0 <= x06 <= 0)
assume(0 <= x07 <= 0)
assume(0 <= x08 <= 0)
assume(0 <= x09 <= 0)
assume(1 <= x010 <= 1)

x10 = (-0.176381)*x00 + (0.255288)*x01 + (0.134367)*x02 + (0.219695)*x03 + (-0.158256)*x04 + (0.257400)*x05 + (0.429901)*x06 + (-0.215020)*x07 + (-0.248879)*x08 + (-0.174564)*x09 + (-0.236890)*x010 + (0.722254)*x011 + (0.948223)*x012 + (-0.014475)*x013 + (0.402999)*x014 + (-0.121757)*x015 + (0.238699)*x016 + (-0.047149)*x017 + (-0.031694)*x018 + (-0.004345)
x11 = (-0.614945)*x00 + (0.428670)*x01 + (-0.254079)*x02 + (0.007457)*x03 + (0.137169)*x04 + (0.169467)*x05 + (0.313271)*x06 + (-0.152268)*x07 + (-0.257944)*x08 + (0.069922)*x09 + (-0.173442)*x010 + (-1.218910)*x011 + (-0.087179)*x012 + (0.082008)*x013 + (-0.215567)*x014 + (-0.127173)*x015 + (0.361749)*x016 + (0.566521)*x017 + (-0.046853)*x018 + (0.059474)
x12 = (0.461141)*x00 + (-0.463049)*x01 + (-0.194844)*x02 + (0.302225)*x03 + (-0.126619)*x04 + (-0.212379)*x05 + (-0.417300)*x06 + (-0.247720)*x07 + (-0.049813)*x08 + (0.112240)*x09 + (-0.190878)*x010 + (0.214388)*x011 + (0.702215)*x012 + (0.229598)*x013 + (-0.694633)*x014 + (0.298917)*x015 + (0.096875)*x016 + (-0.235219)*x017 + (-0.031773)*x018 + (-0.074578)
x13 = (0.395337)*x00 + (0.133710)*x01 + (0.398291)*x02 + (0.061065)*x03 + (0.176328)*x04 + (0.327215)*x05 + (0.377684)*x06 + (0.065898)*x07 + (0.181120)*x08 + (0.084705)*x09 + (0.160146)*x010 + (-1.220180)*x011 + (-1.162299)*x012 + (0.095897)*x013 + (0.363520)*x014 + (-0.194693)*x015 + (0.034721)*x016 + (-0.096965)*x017 + (0.104423)*x018 + (0.104535)
x14 = (-0.166088)*x00 + (-0.227722)*x01 + (0.199718)*x02 + (0.067818)*x03 + (-0.200638)*x04 + (-0.239776)*x05 + (-0.172506)*x06 + (-0.341131)*x07 + (-0.143765)*x08 + (-0.158504)*x09 + (-0.103501)*x010 + (1.288083)*x011 + (0.432059)*x012 + (0.335868)*x013 + (-0.199739)*x014 + (-0.130234)*x015 + (0.509266)*x016 + (0.250009)*x017 + (0.388201)*x018 + (0.066210)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (0.640621)*x10 + (-0.573731)*x11 + (0.246119)*x12 + (-0.262054)*x13 + (0.469129)*x14 + (0.163515)
x21 = (-0.154126)*x10 + (-0.305663)*x11 + (-0.533692)*x12 + (0.767974)*x13 + (0.390266)*x14 + (0.065860)
x22 = (-0.526231)*x10 + (-0.865446)*x11 + (0.696966)*x12 + (-0.131988)*x13 + (0.224530)*x14 + (-0.085899)
x23 = (-0.369137)*x10 + (0.335443)*x11 + (-0.190867)*x12 + (0.635366)*x13 + (-0.410546)*x14 + (0.163797)
x24 = (-0.364383)*x10 + (0.781415)*x11 + (-0.079497)*x12 + (0.051843)*x13 + (-0.348779)*x14 + (0.076978)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (-0.195749)*x20 + (-0.688691)*x21 + (1.048759)*x22 + (0.647179)*x23 + (-0.342585)*x24 + (0.162591)
x31 = (0.666188)*x20 + (-0.267945)*x21 + (0.607944)*x22 + (-0.530181)*x23 + (0.500374)*x24 + (0.243329)
x32 = (-0.652052)*x20 + (0.636247)*x21 + (0.260386)*x22 + (0.733732)*x23 + (0.511470)*x24 + (0.139559)
x33 = (-0.553650)*x20 + (0.717003)*x21 + (0.385805)*x22 + (0.678441)*x23 + (0.497826)*x24 + (0.105702)
x34 = (-0.486372)*x20 + (-0.839306)*x21 + (0.296202)*x22 + (-0.274376)*x23 + (0.276426)*x24 + (0.093935)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (0.171270)*x30 + (0.801403)*x31 + (-0.642715)*x32 + (0.517609)*x33 + (0.876366)*x34 + (-0.029640)
x41 = (0.007168)*x30 + (1.144865)*x31 + (0.068819)*x32 + (0.239674)*x33 + (-0.572651)*x34 + (0.603885)
x42 = (0.446804)*x30 + (0.101453)*x31 + (0.713946)*x32 + (0.836666)*x33 + (0.627625)*x34 + (-0.072648)
x43 = (0.386080)*x30 + (-0.151819)*x31 + (0.403916)*x32 + (0.842890)*x33 + (0.215149)*x34 + (0.026987)
x44 = (-0.707403)*x30 + (0.617330)*x31 + (-0.497090)*x32 + (-0.742033)*x33 + (0.524009)*x34 + (-0.024925)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (-1.257693)*x40 + (-0.609877)*x41 + (0.154139)*x42 + (0.810221)*x43 + (-0.535772)*x44 + (-0.579417)
x51 = (0.299726)*x40 + (-0.060551)*x41 + (-0.011512)*x42 + (0.208604)*x43 + (-0.604791)*x44 + (-0.293266)
x52 = (-0.261051)*x40 + (0.402681)*x41 + (-0.952128)*x42 + (-0.028799)*x43 + (-0.094560)*x44 + (0.629596)
#
