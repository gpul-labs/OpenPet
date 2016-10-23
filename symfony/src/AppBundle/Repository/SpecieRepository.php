<?php

namespace AppBundle\Repository;

use Doctrine\ORM\EntityRepository;

class SpecieRepository extends EntityRepository
{

    public function filter($request)
    {
        // {{{

        $qb = $this->getEntityManager()->createQueryBuilder();

        $qb->select('s')
            ->from('AppBundle:Specie', 's')
            ->where('s.deletedAt is null')
            ->orderBy('s.id', 'ASC')
            ;

        return $qb->getQuery()->getResult();

        // }}}
    }

}
