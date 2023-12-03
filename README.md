# pythonProject

Bir konsol üzerinden kullanıcı girişi olacak.Kullanıcıdan koordinat düzleminde bir noktanın x ve y noktaları istenecek.
Her kullanıcı girişi yapıldığında arkada yeni bir rastgele noktalarda bir üçgen üretilecek ve kullanıcıdan alınan nokta
bu üretilen üçgenin içinde mi değil mi diye kontrol edecek. Ve her döngünün sonunda kullanıcıya devam mı bitir mi diye sorulacak.
Eğer bitir denirse program sonlanacak.


nokta_konum_dugrulama fonk içerisindeki koddaki işlemler barycentric coordinate system veya barycentric interpolation olarak adlandırılır. Bu sistem, bir üçgenin içindeki belirli bir noktanın konumunu belirlemek için kullanılır. Bu yöntem, üçgenin içindeki noktanın üç köşesi arasındaki ağırlıkları kullanarak hesaplanır.
detT: Bu, üçgenin alanını temsil eden determinandır. Üçgenin köşeleri arasındaki alanı hesaplamak için kullanılır.
alpha, beta, gamma: Bu değerler, üçgenin içindeki bir noktanın barycentric koordinatlarıdır. Alpha, Beta ve Gamma değerleri, üçgenin köşelerine olan uzaklıklarını belirler. Bu değerlerin toplamı her zaman 1'e eşittir.
