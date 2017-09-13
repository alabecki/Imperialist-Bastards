from minor_classes import*
from name_generator import*
	

def create_provinces():

	provinces = {}
	
	Fonie = Province("Fonie", "Bambaki", "food", 1.1, "civilized", "Bambaki")
	Fonie.x = 4
	Fonie.y = 9
	provinces["Fonie"] = Fonie
	
	Fivne = Province("Fivne", "Bambaki", "cotton", 1.1, "civilized", "Bambaki")
	Fivne.x = 5
	Fivne.y = 9
	provinces["Fivne"] = Fivne
	
	Fiten = Province("Fiten", "Bambaki", "food", 1,  "civilized", "Bambaki")
	Fiten.x = 5
	Fiten.y = 10
	provinces["Fiten"] = Fiten

	Sine = Province("Sine", "Bambaki", "cotton", 1.1,  "civilized", "Bambaki" )
	Sine.x = 6
	Sine.y = 9
	provinces["Sine"] = Sine
	
	Siten = Province("Siten", "Bambaki", "coal", 1.1, "civilized", "Bambaki")
	Siten.x = 6
	Siten.y = 10
	provinces["Siten"] = Siten


	Severen = Province("Severen", "Bambaki", "iron", 1.1, "civilized", "Bambaki")
	Severen.x = 7
	Severen.y = 9
	provinces["Severen"] = Severen



	Foleven = Province("Foleven", "Hyle", "wood", 1.2, "civilized", "Hyle")
	Foleven.x = 4
	Foleven.y = 11
	provinces["Foleven"] = Foleven

	
	Fotwee = Province("Fotwee", "Hyle", "wood", 1.2, "civilized", "Hyle" )
	Fotwee.x = 4
	Fotwee.y = 12
	Fotwee.ocean = False
	provinces["Fotwee"] = Fotwee
	
	Threlve = Province("Threlve", "Hyle", "cotton", 1.0, "civilized", "Hyle")
	Threlve.x = 3
	Threlve.y = 12
	provinces["Threlve"] = Threlve
	

	Fothra = Province("Fothra", "Hyle", "coal", 1.1, "civilized", "Hyle")
	Fothra.x = 2
	Fothra.y = 11
	Fothra.ocean = False
	provinces["Fothra"] = Fothra
	
	Threthre = Province("Threthre", "Hyle", "food", 1.1, "civilized", "Hyle")
	Threthre.x = 2
	Threthre.y = 12
	provinces["Threthre"] = Threthre
	
	Tothra = Province("Tothra", "Hyle", "food", 1.0, "civilized", "Hyle")
	Tothra.x = 2
	Tothra.y = 13
	provinces["Tothra"] = Tothra

	
	
	Niten = Province("Niten", "Trope", "food", 1.2, "civilized", "Trope")
	Niten.x = 9
	Niten.y =10
	provinces["Niten"] = Niten

	Teetee = Province("Teetee", "Trope", "food", 1.1, "civilized", "Trope")
	Teetee.x = 10
	Teetee.y = 10
	provinces["Teetee"] = Teetee


	Teaven = Province("Teaven", "Trope", "food", 1.2, "civilized", "Trope")
	Teaven.x = 10
	Teaven.y =11
	provinces["Teaven"] = Teaven
	
	Nineven = Province("Nineven", "Trope", "cotton", 0.9, "civilized", "Trope")
	Nineven.x = 9
	Nineven.y = 11
	Nineven.ocean = False
	provinces["Nineven"] = Nineven
	
	Eateven = Province("Eateven", "Trope", "coal", 1.1, "civilized", "Trope")
	Eateven.x = 8
	Eateven.y = 11
	Eateven.ocean = False
	provinces["Eateven"] = Eateven
	
	Seleven = Province("Seleven", "Trope", "iron", 1.0, "civilized", "Trope")
	Seleven.x = 7
	Seleven.y = 11
	Seleven.ocean = False
	provinces["Seleven"] = Seleven

	
	Seele = Province("Seele", "Sidero", "iron", 1.1, "civilized", "Sidero")
	Seele.x = 6
	Seele.y = 11
	Seele.ocean = False
	provinces["Seele"] = Seele
	
	Sitwee = Province("Sitwee", "Sidero", "iron", 1.1, "civilized", "Sidero")
	Sitwee.x = 6
	Sitwee.y = 12
	provinces["Sitwee"] = Sitwee
	
	Thesee = Province("Thesee", "Sidero", "food", 1.1, "civilized", "Sidero")
	Thesee.x = 6
	Thesee.y = 13
	provinces["Thesee"] = Thesee


	Fithee = Province("Fithee", "Sidero", "coal", 1.2, "civilized", "Sidero")
	Fithee.x = 5
	Fithee.y = 13
	provinces["Fithee"] = Fithee

	Sifoo  = Province("Sifoo", "Sidero", "food", 1, "civilized", "Sidero")
	Sifoo.x = 6
	Sifoo.y = 14
	provinces["Sifoo"] = Sifoo

	
	Fivfoo = Province("Fivfoo", "Sidero", "wood", 1, "civilized", "Sidero")
	Fivfoo.x = 5
	Fivfoo.y = 14
	provinces["Fivfoo"] = Fivfoo

	
	Nifeenee = Province("Nifeenee", "Isorropia", "cotton", 0.9, "civilized", "Isorropia")
	Nifeenee.x = 9
	Nifeenee.y = 15
	provinces["Nifeenee"] = Nifeenee
	
	Efetee = Province("Efetee", "Isorropia", "wood", 1, "civilized", "Isorropia")
	Efetee.x = 8
	Efetee.y = 15
	provinces["Efetee"] = Efetee

	
	Sevfif = Province("Sevfif", "Isorropia", "coal", 1.1, "civilized", "Isorropia")
	Sevfif.x = 7
	Sevfif.y = 15
	provinces["Sevfif"] = Sevfif

	Eigsix = Province("Eigsix", "Isorropia", "food", 1.1, "civilized", "Isorropia")
	Eigsix.x = 8
	Eigsix.y = 16
	provinces["Eigsix"] = Eigsix

	Seasix = Province("Seasix", "Isorropia", "iron", 1.1, "civilized", "Isorropia")
	Seasix.x = 7
	Seasix.y = 16
	provinces["Seasix"] = Seasix

	Eisev = Province("Eisev", "Isorropia", "food", 1.1, "civilized", "Isorropia")
	Eisev.x = 8
	Eisev.y = 17
	Eisev.ocean = True
	provinces["Eisev"] = Eisev



	Sevteeve  = Province("Sevteeve", "Karbouno", "coal", 1.3, "civilized", "Karbouno")
	Sevteeve.x = 4
	Sevteeve.y = 14
	provinces["Sevteeve"] = Sevteeve 
	
	Fogaro = Province("Fogaro", "Karbouno", "coal", 1.2, "civilized", "Karbouno")
	Fogaro.x = 4
	Fogaro.y = 15
	provinces["Fogaro"] = Fogaro
	
	Sartarva = Province("Sartarva", "Karbouno", "iron", 1.1, "civilized", "Karbouno")
	Sartarva.x = 5
	Sartarva.y = 16
	Sartarva.ocean = False
	provinces["Sartarva"] = Sartarva
	
	Sifoto = Province("Sifoto",   "Karbouno", "food", 1.0, "civilized", "Karbouno")
	Sifoto.x = 4
	Sifoto.y = 16
	Sifoto.ocean = False
	provinces["Sifoto"] = Sifoto

	Togema = Province("Togema",  "Karbouno", "food", 1.1, "civilized", "Karbouno")
	Togema.x = 5
	Togema.y = 17
	Togema.ocean = False
	provinces["Togema"] = Togema
	
	Sisivo = Province("Sisivo", "Karbouno", "wood", 1.0, "civilized", "Karbouno")
	Sisivo.x = 4
	Sisivo.y = 17
	Sisivo.ocean = False
	provinces["Sisivo"] = Sisivo

	
	Enee = Province("Enee", "Situs", "cotton", 0.8, "civilized", "Situs")
	Enee.x = 8
	Enee.y = 9
	Enee.ocean = False
	provinces["Enee"] = Enee

	Tennini = Province("Tennini", "Situs", "food", 1.1, "civilized", "Situs")
	Tennini.x = 9
	Tennini.y = 10
	Tennini.ocean = False
	provinces["Tennini"] = Tennini
	
	Perma = Province("Perma", "Hythen", "wood", 1.1, "civilized", "Hythen")
	Perma.x = 4
	Perma.y = 10
	Perma.ocean = False
	provinces["Perma"] = Perma

	Urten = Province("Urten", "Hythen", "food", 0.9, "civilized", "Hythen")
	Urten.x = 3
	Urten.y = 10
	Urten.ocean = False
	provinces["Urten"] = Urten
	
	Tomski = Province("Tomski", "Intero", "gold", 1.1, "civilized", "Intero")
	Tomski.x = 5
	Tomski.y = 11
	Tomski.ocean = False
	provinces["Tomski"] = Tomski

	Teetsito = Province("Teetsito", "Intero", "iron", 1, "uncivilized", "Intero")
	Teetsito.x = 5
	Teetsito.y = 12
	Teetsito.ocean = False
	provinces["Teetsito"] = Teetsito


	Irku = Province("Irku",  "Kora", "coal", 1.2, "uncivilized", "Kora")
	Irku.x = 3
	Irku.y = 14
	Irku.ocean = False
	provinces["Irku"] = Irku


	Yakutsk = Province("Yakutsk",  "Kora", "food", 1.0, "uncivilized", "Kora")
	Yakutsk.x = 5
	Yakutsk.y = 24
	Yakutsk.ocean = False
	provinces["Yakutsk"] = Yakutsk

	Okho = Province("Okho", "Southo", "wood", 1.0, "uncivilized", "Southo")
	Okho.x = 12
	Okho.y = 11
	provinces["Okho"] = Okho

	Findee = Province("Findee", "Southo", "food", 1.1, "civilized", "Southo")
	Findee.x = 11
	Findee.y = 11
	provinces["Findee"] = Findee

	Napa = Province("Napa", "Cindra", "food", 1.1, "civilized", "Cindra")
	Napa.x = 8
	Napa.y = 14
	provinces["Napa"] = Napa
	Lazo = Province("Lazo", "Cindra", "coal", 1.0, "civilized", "Cindra")
	Lazo.x = 7
	Lazo.y = 14
	provinces["Lazo"] = Lazo

	Vene = Province("Vene", "Estos", "cotton", 0.8, "civilized", "Estos")
	Vene.x = 10
	Vene.y = 16
	provinces["Vene"] = Vene
	Eta = Province("Eta", "Estos", "food", 1, "civilized", "Estos")
	Eta.x = 9
	Eta.y = 16
	provinces["Eta"] = Eta

	Silseva = Province("Silseva","Lian",  "iron", 1.0, "civilized", "Lian")
	Silseva.x = 6
	Silseva.y = 16
	provinces["Silseva"] = Silseva

	Bosa = Province("Bosa", "Lian", "food", 1.0, "civilized", "Lian")
	Bosa.x = 6
	Bosa.y = 17
	provinces["Bosa"] = Bosa



	Garia = Province("Garia", "Bulgo", "wood", 1.0, "civilized", "Bulgo")
	Garia.x = 4
	Garia.x = 10
	provinces["Garia"] = Garia

	Sebia = Province("Sebia", "Bulgo", "food", 1.0, "civilized", "Bulgo")
	Sebia.x = 3
	Sebia.y = 10
	provinces["Sebia"] = Sebia



	Grayto = Province("Grayto", "Kaygree", "oil", 1.0, "old", "Kaygree")
	Grayto.x = 9
	Grayto.y = 3
	provinces["Grayto"] = Grayto
	Tura = Province("Tura", "Kaygree", "rubber", 0.9, "old", "Kaygree")
	Tura.x = 9
	Tura.y =2
	provinces["Tura"] = Tura
	EastKish = Province("EastKish", "Kish", "spice", 0.9, "old", "Kish")
	EastKish.x = 11
	EastKish.y = 4
	provinces["EastKish"] = EastKish
	WestKish = Province("WestKish", "Kish", "gold", 1.1, "old", "Kish")
	WestKish.x = 11
	WestKish.y = 3
	provinces["WestKish"] = WestKish

	EastRabus = Province("EastRabus", "Rabus", "food", 1.0, "old", "Rabus")
	EastRabus.x = 13
	EastRabus.y = 4
	provinces["EastRabus"] = EastRabus
	WestRabus = Province("WestRabus", "Rabus", "gold", 1.0, "old", "Rabus")
	WestRabus.x = 13
	WestRabus.y = 3
	provinces["WestRabus"] = WestRabus


	EastSparko = Province("EastSparko", "Sparko", "food", 1.0, "old", "Sparko")
	EastSparko.x = 15
	EastSparko.y = 4
	provinces["EastSparko"] = EastSparko

	WestSparko = Province("WestSparko", "Sparko", "rubber", 1.0, "old", "Sparko")
	WestSparko.x = 15
	WestSparko.y = 3
	provinces["WestSparko"] = WestSparko

	NorthArgos = Province("NorthArgos", "Argos", "food", 1.0, "old", "Argos")
	NorthArgos.x = 16
	NorthArgos.y = 7
	provinces["NorthArgos"] = NorthArgos
	
	SouthArgos = Province("SouthArgos", "Argos", "dyes", 0.9, "old", "Argos")
	SouthArgos.x = 17
	SouthArgos.y = 7
	provinces["SouthArgos"] = SouthArgos
	
	NorthMancha = Province("NorthMancha", "Mancha", "cotton", 0.9, "old", "Mancha")
	NorthMancha.x = 16
	NorthMancha.y = 10
	provinces["NorthMancha"] = NorthMancha

	SouthMancha = Province("SouthMancha", "Mancha", "dyes", 0.9, "old", "Mancha")
	SouthMancha.x = 16
	SouthMancha.y = 10
	provinces["SouthMancha"] = SouthMancha

	NorthGelder = Province("NorthGelder", "Gelder", "spice", 1.0, "old", "Gelder")
	NorthGelder.x = 16
	NorthGelder.y = 14
	provinces["NorthGelder"] = NorthGelder
	SouthGelder = Province("SouthGelder", "Gelder", "food", 1, "old", "Gelder")
	SouthGelder.x = 17
	SouthGelder.y = 14
	provinces["SouthGelder"] = SouthGelder


	NorthPorta = Province("NorthPorta", "Porta", "spice", 1.0, "old", "Porta")
	NorthPorta.x = 16
	NorthPorta.y = 17
	provinces["NorthPorta"] = NorthPorta

	SouthPorta = Province("SouthPorta", "Porta", "oil", 1.0, "old", "Porta")
	SouthPorta.x = 17
	SouthPorta.y = 17
	provinces["SouthPorta"] = SouthPorta

	WestNorra = Province("WestNorra", "Norra", "spice", 1.0, "old", "Norra")
	WestNorra.x = 15
	WestNorra.y = 20
	provinces["WestNorra"] = WestNorra
	EastNorra = Province("EastNorra", "Norra", "rubber", 1.0, "civilized", "Norra")
	EastNorra.x = 15
	EastNorra.y = 21
	provinces["EastNorra"] = EastNorra

	WestWego = Province("WestWego", "Wego", "food", 1.0, "civilized", "Wego")
	WestWego.x = 13
	WestWego.y = 20
	provinces["WestWego"] = WestWego

	EastWego = Province("EastWego", "Wego", "oil", 1.0, "civilized", "Wego")
	EastWego.x = 13
	EastWego.y = 21
	provinces["EastWego"] = EastWego

	WestArbaca = Province("WestArbaca", "Arbaca", "rubber", 1.0, "old", "Arbaca")
	WestArbaca.x = 13
	WestArbaca.y = 13
	provinces["WestArbaca"] = WestArbaca
	EastArbaca = Province("EastArbaca", "Arbaca", "oil", 1.0, "old", "Arbaca")
	EastArbaca.x = 14
	EastArbaca.y = 13
	EastArbaca.ocean = False
	provinces["EastArbaca"] = EastArbaca

	WestEgaro = Province("WestEgaro", "Egaro", "spice", 1.0, "old", "Egaro")
	WestEgaro.x = 9
	WestEgaro.y = 22
	WestEgaro.ocean = False
	provinces["WestEgaro"] = WestEgaro
	EastEgaro = Province("EastEgaro",  "Egaro", "food", 0.8, "old", "Egaro")
	EastEgaro.x = 9
	EastEgaro.y = 23
	EastEgaro.ocean = False
	provinces["EastEgaro"] = EastEgaro

	return provinces
	