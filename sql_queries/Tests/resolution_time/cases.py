from sql_queries.meta.aggs import ResolutionTime


iterations_in_non_bugs_only = {
    ResolutionTime.ticket_scid.name: [1, 2, 4],
    ResolutionTime.resolution_in_hours.name: [0, 1, 3],
    ResolutionTime.lifetime_in_hours.name: [0, 1, 3],
}

bugs_only_after_most_recent_conversion_to_bug = {
    ResolutionTime.ticket_scid.name: [11, 22],
    ResolutionTime.resolution_in_hours.name: [1, 2],
    ResolutionTime.lifetime_in_hours.name: [1, 2],
}

bugs_only_between_period = {
    ResolutionTime.ticket_scid.name: [22],
    ResolutionTime.resolution_in_hours.name: [5],
    ResolutionTime.lifetime_in_hours.name: [5],
}

only_bugs_with_audit = {
    ResolutionTime.ticket_scid.name: [22],
    ResolutionTime.resolution_in_hours.name: [2],
    ResolutionTime.lifetime_in_hours.name: [2],
}

bugs_with_only_closed_audit_records = {
    ResolutionTime.ticket_scid.name: [22],
    ResolutionTime.resolution_in_hours.name: [2],
    ResolutionTime.lifetime_in_hours.name: [2],
}

resolution_time_includes_iterations_and_bugs = {
    ResolutionTime.ticket_scid.name: [3, 11],
    ResolutionTime.resolution_in_hours.name: [4, 22],
    ResolutionTime.lifetime_in_hours.name: [98, 22],
}
