output "name" {
  description = "Configured Incus instance name."
  value       = incus_instance.this.name
}

output "project" {
  description = "Configured Incus project."
  value       = incus_instance.this.project
}

output "instance_type" {
  description = "Configured Incus instance type."
  value       = incus_instance.this.type
}
