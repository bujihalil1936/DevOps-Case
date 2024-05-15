Infrastructure Design

Birden fazla Linux distrosuyla 5000'den fazla VM'yi yönetmek ve toplu işlemleri verimli bir şekilde gerçekleştirmek için Configuration Management Tool olarak (Ansible gibi), Orchestration Tool olarak (Kubernetes gibi) ve Monitoring Tool kullanırsak (Prometheus ve Grafana ) gibi toollardan yararlanarak bir altyapı tasarlarım.

Bileşenler;

--- Configuration Management Tool: Ansible

Ansible agetless özelliğe sahip olduğu için ve iletişim için SSH'yi kullanır, bu da onu heterojen bir ortamı yönetmeye uygun hale getirir.
Playbook'lar konfigürasyonları ve taskları tanımlar, kernel parametrelerinin güncellenmesi gibi toplu işlemlere izin verir.  

--- Orchestration Tool: Kubernetes

Kubernetes, declarative konfigürasyon ve otomasyon sağlayarak konteynerleştirilmiş iş yüklerini ve hizmetleri yönetmeye yardımcı olabilir.
VM'ler ise label ve selector kullanarak gruplandırabilir ve işlemlerde esneklik sağlar.

--- Monitoring Tool: Prometheus and Grafana

Prometheus, VM'lerden ve servislerden metrikler toplarken Grafana görselleştirme sağlar.
Administratorleri belirli koşullar veya hatalar hakkında bilgilendirmek için notification rulelar belirlenebilir.

--- Inventory Management: CMDB (Configuration Management Database)

Bir CMDB, çalışan uygulama, işletim sistemi dağıtımı ve yapılandırma ayrıntıları gibi özellikler dahil olmak üzere VM'ler hakkındaki meta dataları depolayabilir.
Bu veritabanı, hedeflenen işlemler için dinamik olarak Ansible inventorileri oluşturmak için kullanılır.

Infrastructure Genel Bakış Hakkında:

Inventory Management:

VM özelliklerini ve konfigürasyonlarını korumak için bir CMDB kullanın.
VM'leri özelliklerle etiketleyin (örneğin, RabbitMQ çalıştırma, işletim sistemi türü).

Sanal Makineleri Gruplayın ve Hedefleyin:

Ansible ve CMDB verilerini kullanarak dinamik envanterler oluşturun.
Etiketleri ve etiketleri kullanarak VM'leri özelliklere göre gruplandırın.

Toplu İşlemleri Tanımlayın:

Yaygın görevler için Ansible çalışma kitapları yazın (örneğin, çekirdek parametrelerini güncellemek).
VM gruplarına dayalı yapılandırmaları uygulamak için Ansible'ın güçlü şablonunu kullanın.

Toplu İşlemleri Yürütün:

Ansible playbooklarını dinamik inventorlere karşı çalıştırın.
Değişiklikleri tutarlı bir şekilde uygulamak için idempotency sağlayın.

Monitoring :

VM'lerin durumunu ve sağlığını izlemek için Prometheus'u kullanın.
Metrikleri görselleştirmek ve kritik durumlar için uyarılar ayarlamak için Grafana dashboardları kurun.


Örnek Flow : RabbitMQ VM'ler için fs.file-max Çekirdek Parametresini Güncelleme

Etiketleme ve Envanter:

CMDB'deki tüm RabbitMQ VM'lerini etiketleyin.

RabbitMQ ile etiketlenmiş VM'ler için bir Ansible inventory oluşturun.


- name: Update fs.file-max for RabbitMQ VMs
  hosts: rabbitmq_vms
  tasks:
    - name: Set fs.file-max to 500000
      sysctl:
        name: fs.file-max
        value: 500000
        state: present
        reload: yes

ansible-playbook -i inventory/rabbitmq_vms.yml update_fs_file_max.yml


Monitoring:

İşlemin başarısını gösteren metrikler için Prometheus'u kontrol edebiliriz.
Metrikleri görselleştirmek ve değişikliklerin doğru şekilde uygulandığından emin olmak için Grafana'yı kullanabiliriz.

https://excalidraw.com/#json=VwjS8llGpMZmHihcfTjQl,EryTyAEKC-I79zQ7vTRxKg