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

output "ipv4_address" {
  description = "Primary IPv4 address reported by Incus when available."
  value       = try(incus_instance.this.ipv4_address, "")
}

output "ipv6_address" {
  description = "Primary IPv6 address reported by Incus when available."
  value       = try(incus_instance.this.ipv6_address, "")
}
