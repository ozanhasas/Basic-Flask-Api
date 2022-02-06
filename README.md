# bcfm-case

Docker image oluşturmak için yani build almak için kullanılan komut. "-t" ile image'ın adını ve tagını yazıyoruz.

```sh
docker build -t flask-api-new:v1 . 
```

Build ettiğim image'ı bir portta(localde) çalıştırmak için kullanılan komut. "-d" docker containerının backgroundta çalışmasını sağlıyor. "-p" ise bir portta publish etmeyi sağlıyor.

```sh
docker run -d -p 5000:5000 flask-api-new:v1
```
