terraform {
  required_version = ">= 1.8"
}

module "reference_environment" {
  source = "../../terraform/modules/reference_environment"

  name         = "hyperion-local"
  cluster_cidr = "192.0.2.0/24"
  service_cidr = "198.51.100.0/24"
}

output "environment" {
  description = "Synthetic local reference values; no external resources are created."
  value       = module.reference_environment.environment
}
