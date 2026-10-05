terraform {
  required_version = ">= 1.8"
}

module "reference_environment" {
  source       = "../../terraform/modules/reference_environment"
  name         = "hyperion-local"
  cluster_cidr = "10.42.0.0/16"
  service_cidr = "10.43.0.0/16"
}

output "environment" {
  value = module.reference_environment.environment
}
