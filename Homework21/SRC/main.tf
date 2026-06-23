provider "aws" {
  region = "eu-central-1"
}

resource "aws_instance" "web" {
  count         = 2
  ami           = "ami-0c55b159cbfafe1f0" # замінимо пізніше
  instance_type = "t2.micro"

  tags = {
    Name = "HW21-${count.index}"
  }
}

output "public_ips" {
  value = aws_instance.web[*].public_ip
}
resource "local_file" "ansible_inventory" {
  content  = templatefile("${path.module}/inventory.tpl", { public_ips = aws_instance.web[*].public_ip })
  filename = "${path.module}/inventory.ini"
}
