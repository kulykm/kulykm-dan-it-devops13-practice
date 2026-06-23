resource "aws_security_group" "web_sg" {
  name   = "hw20-web-sg"
  vpc_id = var.vpc_id

  dynamic "ingress" {
    for_each = var.list_of_open_ports
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web_server" {
  ami           = "ami-0a49b025fffbbdac6"
  instance_type = "t2.micro"

  vpc_security_group_ids      = [aws_security_group.web_sg.id]
  associate_public_ip_address = true

  user_data = <<EOF
#!/bin/bash
apt update -y
apt install nginx -y
systemctl start nginx
EOF
}
