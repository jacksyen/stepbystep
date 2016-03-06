package {{base_package}}.domain.{{sub_domain}}

import javax.persistence.*;
import javax.validation.constraints.NotNull;

@Entity
@Table

public class {{entity_name}}{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

   {% for member in members %}
       @NotNull
       @Column
       private {{member.type}} {{member.name}};
   {% endfor %}
}