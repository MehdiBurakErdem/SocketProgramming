# Python Socket Uygulaması
 İlk aşamada basic Python projeleri incelenebilir, sonrasında ise socket programlama örneğine geçebilirsiniz.

# 02_Socket
Projede **client–server–client** yapısı kullanılmaktadır. **Client 1**, gönderilecek veriyi alır ve bu veriyi bir **parity bit** (eşlik biti) ile birlikte paket haline getirir. Bu parity bit, iletim sırasında oluşabilecek hataların tespit edilebilmesi için kullanılmaktadır.

Oluşturulan paket, ara katman olarak çalışan **Server**’a gönderilir. Server tarafında, gerçek bir iletişim hattı simüle edilerek veriye bilerek rastgele hata yüklemesi yapılır. Bu hata yüklemesi iki farklı şekilde uygulanmaktadır:

- **Character Substitution (karakter değiştirme)**
- **Character Deletion (karakter silme)**

Hata uygulanmış paket daha sonra **Client 2**’ye iletilir. Client 2, gelen verinin **parity bit**’ini tekrar hesaplar ve gönderilen parity bilgisi ile karşılaştırır. Bu karşılaştırma sonucunda, verinin doğru şekilde ulaşıp ulaşmadığı tespit edilir.

Proje, öğrenme ve deneme amaçlı hazırlanmıştır.
