terraform {
  backend "s3" {
    bucket = "terraform-state-danit-devops"
    key    = "maksym/homework20/terraform.tfstate"
    region = "eu-central-1"
  }
}
