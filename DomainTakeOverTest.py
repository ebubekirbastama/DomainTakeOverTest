import dns.resolver

# Potansiyel takeover hedefleri listesi
BILINEN_TAKEOVER_PATLARI = [
    "aws", "s3.amazonaws.com", "github.io", "herokuapp.com",
    "pages.dev", "readthedocs.io", "unbouncepages.com", 
    "azurewebsites.net", "cloudfront.net", "shopify.com",
    "wordpress.com", "tumblr.com", "bitbucket.io", "fastly.net",
    "cdn.cloudflare.net", "cargocollective.com", "ghost.io",
    "surge.sh", "pantheon.io", "smugmug.com"
]

# Kontrol edilecek subdomain'ler
SUBDOMAIN_LIST = [
    "mail", "ftp", "www", "blog", "dev", "test", "staging",
    "admin", "api", "shop", "cdn", "images"
]

# Kontrol edilecek domain'ler
DOMAINS = [
    "orneksite.com",
    "orneksite.com",

]

def cname_kontrol(domain):
    try:
        answers = dns.resolver.resolve(domain, 'CNAME')
        for answer in answers:
            cname_hedefi = str(answer.target).lower()
            for pattern in BILINEN_TAKEOVER_PATLARI:
                if pattern in cname_hedefi:
                    return f"Potansiyel Takeover: {domain} -> {cname_hedefi}"
            return f"Güvenli: {domain} -> {cname_hedefi}"
        return f"Güvenli: {domain} (CNAME bulunamadı)"
    except dns.resolver.NoAnswer:
        return f"CNAME kaydı bulunamadı: {domain}"
    except dns.resolver.NXDOMAIN:
        return f"Domain mevcut değil: {domain}"
    except Exception as e:
        return f"{domain} kontrol edilirken hata oluştu: {e}"

def subdomain_taramasi(domain):
    subdomain_sonuclari = []
    for sub in SUBDOMAIN_LIST:
        alt_domain = f"{sub}.{domain}"
        sonuc = cname_kontrol(alt_domain)
        subdomain_sonuclari.append(sonuc)
    return subdomain_sonuclari

def main():
    tüm_sonuçlar = []
    takeover_riskleri = []

    for domain in DOMAINS:
        # Ana domain kontrolü
        ana_domain_sonucu = cname_kontrol(domain)
        print(ana_domain_sonucu)
        tüm_sonuçlar.append(ana_domain_sonucu)

        if "Potansiyel Takeover" in ana_domain_sonucu:
            takeover_riskleri.append(ana_domain_sonucu)

        # Subdomain taraması
        subdomain_sonuçları = subdomain_taramasi(domain)
        for sonuc in subdomain_sonuçları:
            print(sonuc)
            tüm_sonuçlar.append(sonuc)
            if "Potansiyel Takeover" in sonuc:
                takeover_riskleri.append(sonuc)

    # Sonuçları kaydet
    with open("sonuclar.txt", "w") as genel_dosya:
        genel_dosya.write("\n".join(tüm_sonuçlar))
    with open("takeover_riskleri.txt", "w") as risk_dosya:
        risk_dosya.write("\n".join(takeover_riskleri))

    print("Kontrol tamamlandı. Sonuçlar 'sonuclar.txt' ve 'takeover_riskleri.txt' dosyalarına kaydedildi.")

if __name__ == "__main__":
    main()
