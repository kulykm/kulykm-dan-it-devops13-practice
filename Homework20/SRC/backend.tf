terraform {
  backend "s3" {
    bucket = "terraform-state-mkulyk-2026"
    key    = "maksym/homework20/terraform.tfstate"
    region = "eu-central-1"
  }
}
