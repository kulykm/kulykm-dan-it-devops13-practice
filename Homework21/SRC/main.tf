provider "aws" {
  region = "eu-central-1"
}

resource "aws_instance" "web" {
  count         = 2
  ami           = "ami-002cae6b67f1a7688"
  instance_type = "t2.micro"
  key_name      = "maxim-key"

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
