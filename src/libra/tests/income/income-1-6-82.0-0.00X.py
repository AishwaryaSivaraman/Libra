x00 = float(input())
x01 = float(input())
x02 = float(input())
x03 = float(input())
x04 = float(input())
x05 = float(input())
x06 = float(input())
x07 = float(input())
x08 = float(input())
x09 = float(input())
x010 = float(input())
x011 = float(input())
x012 = float(input())
x013 = float(input())
x014 = float(input())
x015 = float(input())
x016 = float(input())

x10 = (-0.616228)*x00 + (0.353312)*x01 + (0.098172)*x02 + (0.354035)*x03 + (0.497933)*x04 + (-0.240981)*x05 + (0.154548)*x06 + (-0.048201)*x07 + (0.049456)*x08 + (0.438842)*x09 + (0.475519)*x010 + (-0.269260)*x011 + (0.212527)*x012 + (-0.170275)*x013 + (-0.091637)*x014 + (0.316627)*x015 + (-0.364813)*x016 + (0.093376)
x11 = (0.168737)*x00 + (0.083673)*x01 + (-0.329627)*x02 + (0.415378)*x03 + (0.101875)*x04 + (1.077246)*x05 + (0.101674)*x06 + (0.143982)*x07 + (0.261540)*x08 + (0.201860)*x09 + (-0.333080)*x010 + (0.485502)*x011 + (-0.120572)*x012 + (0.365385)*x013 + (0.284709)*x014 + (0.386148)*x015 + (0.368933)*x016 + (0.170581)
x12 = (0.017339)*x00 + (-0.365902)*x01 + (-0.455755)*x02 + (0.177206)*x03 + (0.329034)*x04 + (-0.114585)*x05 + (0.287648)*x06 + (-0.070069)*x07 + (-0.067373)*x08 + (0.223956)*x09 + (-0.108179)*x010 + (-0.423693)*x011 + (-0.126773)*x012 + (-0.110752)*x013 + (-0.242921)*x014 + (-0.320389)*x015 + (-0.231946)*x016 + (-0.052725)
x13 = (-0.160831)*x00 + (-0.057984)*x01 + (-0.073837)*x02 + (0.074713)*x03 + (0.595708)*x04 + (-0.791697)*x05 + (0.569096)*x06 + (-0.065442)*x07 + (0.220393)*x08 + (0.227750)*x09 + (-0.065072)*x010 + (0.487254)*x011 + (0.251288)*x012 + (0.463501)*x013 + (0.484340)*x014 + (0.323835)*x015 + (-0.329937)*x016 + (0.169646)
x14 = (0.239571)*x00 + (-0.221110)*x01 + (-0.265842)*x02 + (-0.289654)*x03 + (0.584452)*x04 + (-0.051268)*x05 + (-0.203065)*x06 + (-0.157072)*x07 + (0.330201)*x08 + (0.187362)*x09 + (0.348891)*x010 + (0.135421)*x011 + (-0.141576)*x012 + (0.356333)*x013 + (-0.202748)*x014 + (0.314023)*x015 + (0.105212)*x016 + (-0.150308)
x15 = (0.401510)*x00 + (-0.028410)*x01 + (0.437623)*x02 + (0.006259)*x03 + (-0.096383)*x04 + (0.014824)*x05 + (0.276891)*x06 + (-0.209061)*x07 + (-0.392703)*x08 + (-0.063451)*x09 + (0.078515)*x010 + (0.100048)*x011 + (0.405267)*x012 + (0.035175)*x013 + (0.174242)*x014 + (-0.222245)*x015 + (0.518536)*x016 + (-0.100988)
#
x10 = x10 if x10 > 0 else 0
x11 = x11 if x11 > 0 else 0
x12 = x12 if x12 > 0 else 0
x13 = x13 if x13 > 0 else 0
x14 = x14 if x14 > 0 else 0
x15 = x15 if x15 > 0 else 0

x20 = (-0.062599)*x10 + (-0.295815)*x11 + (0.366664)*x12 + (0.123192)*x13 + (0.395553)*x14 + (0.025550)*x15 + (-0.164523)
x21 = (-0.484577)*x10 + (0.444071)*x11 + (0.348217)*x12 + (-1.010945)*x13 + (-0.583627)*x14 + (0.533138)*x15 + (-0.083202)
x22 = (-0.634560)*x10 + (0.384127)*x11 + (0.483589)*x12 + (-0.997567)*x13 + (-0.602208)*x14 + (0.420473)*x15 + (0.126796)
x23 = (-0.082569)*x10 + (-0.503676)*x11 + (-0.527615)*x12 + (-0.514866)*x13 + (0.459534)*x14 + (-0.228888)*x15 + (-0.040535)
x24 = (-0.206833)*x10 + (-0.215652)*x11 + (-0.520440)*x12 + (-0.463384)*x13 + (0.001982)*x14 + (-0.487480)*x15 + (0.000000)
x25 = (-0.277929)*x10 + (0.344757)*x11 + (0.257210)*x12 + (-0.883018)*x13 + (-0.831592)*x14 + (-0.319525)*x15 + (0.065889)
#
x20 = x20 if x20 > 0 else 0
x21 = x21 if x21 > 0 else 0
x22 = x22 if x22 > 0 else 0
x23 = x23 if x23 > 0 else 0
x24 = x24 if x24 > 0 else 0
x25 = x25 if x25 > 0 else 0

x30 = (0.225184)*x20 + (-0.850366)*x21 + (-1.031120)*x22 + (-0.279187)*x23 + (-0.744597)*x24 + (-1.393554)*x25 + (1.772279)
x31 = (0.718021)*x20 + (0.635054)*x21 + (1.062907)*x22 + (0.270934)*x23 + (-0.717102)*x24 + (-0.006350)*x25 + (-1.772279)

if x31 <= x30:
    raise ValueError