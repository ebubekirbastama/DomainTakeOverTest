# Domain ve Subdomain Takeover Riski Kontrol Aracı

Bu Python betiği, verilen domain ve subdomain'lerde potansiyel takeover (ele geçirme) risklerini tespit etmek amacıyla CNAME kayıtlarını kontrol eder. Eğer domain ya da subdomain, bilinen takeover hedeflerinden birine yönlendirilmişse, bu durum "Potansiyel Takeover" olarak işaretlenir. Ayrıca, sonuçlar `sonuclar.txt` ve `takeover_riskleri.txt` dosyalarına kaydedilir.

## Özellikler

- **CNAME Kontrolü**: Verilen domain ve subdomain'lerde CNAME kaydı bulunup bulunmadığı kontrol edilir.
- **Takeover Riski**: Domain veya subdomain, bilinen takeover hedeflerinden birine yönlendirildiyse, potansiyel takeover riski tespit edilir.
- **Sonuç Dosyaları**: 
  - `sonuclar.txt`: Tüm domain ve subdomain'lerin kontrol sonuçlarını içerir.
  - `takeover_riskleri.txt`: Potansiyel takeover riski taşıyan domain ve subdomain'lerin listesini içerir.

## Bilinen Takeover Hedefleri

Aşağıdaki hizmetler, subdomain takeover saldırılarına karşı hassas olabilir. Betik, bu hedeflerden birine yönlendirilmiş CNAME kayıtlarını tespit eder:

- aws
- s3.amazonaws.com
- github.io
- herokuapp.com
- pages.dev
- readthedocs.io
- unbouncepages.com
- azurewebsites.net
- cloudfront.net
- shopify.com
- wordpress.com
- tumblr.com
- bitbucket.io
- fastly.net
- cdn.cloudflare.net
- cargocollective.com
- ghost.io
- surge.sh
- pantheon.io
- smugmug.com

## Kurulum

1. Gerekli bağımlılığı yükleyin:
    ```bash
    pip install dnspython
    ```

2. Python betiğini çalıştırın:
    ```bash
    python takeover_kontrol.py
    ```

## Kullanım

- Betik çalıştırıldığında, belirtilen domain ve subdomain'lerde CNAME kayıtları kontrol edilir.
- Sonuçlar şu dosyalarda saklanır:
    - **sonuclar.txt**: Tüm domain ve subdomain'lerin kontrol sonuçları.
    - **takeover_riskleri.txt**: Potansiyel takeover riski taşıyan domain ve subdomain'ler.

## Lisans ve Feragat

- **Lisans**: Bu proje Apache-2.0 license Lisansı altında lisanslanmıştır.
- **Feragat**: Bu betik yalnızca güvenlik testleri ve araştırmaları için kullanılmalıdır. İzinsiz kullanım yasadışıdır ve etik olmayan bir şekilde kullanılmamalıdır.

## Katkı

Herhangi bir katkıda bulunmak isterseniz, pull request gönderebilir ya da issues sekmesinden geri bildirimde bulunabilirsiniz.

