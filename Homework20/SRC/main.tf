module "web_server" {
  source = "./modules/web"

  vpc_id             = var.vpc_id
  list_of_open_ports = var.list_of_open_ports
}
