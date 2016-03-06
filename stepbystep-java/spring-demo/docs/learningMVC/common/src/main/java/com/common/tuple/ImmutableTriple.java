package com.springdemo.learningMVC.common.src.main.java.com.common.tuple;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * An immutable triple consisting of three {@code Object} elements.
 * <p>
 * Although the implementation is immutable, there is no restriction on the objects
 * that may be stored. If mutable objects are stored in the triple, then the triple
 * itself effectively becomes mutable. The class is also {@code final}, so a subclass
 * can not add undesirable behaviour.
 * <p>
 * #ThreadSafe# if all three objects are thread-safe
 *
 * @param <L> the left element type
 * @param <M> the middle element type
 * @param <R> the right element type
 * @version $Id: ImmutableTriple.java 290 2014-10-27 08:48:18Z fuchun $
 */
public final class ImmutableTriple<L, M, R> extends Triple<L, M, R> {
    /**
     * Serialization version
     */
    private static final long serialVersionUID = 1L;
    /**
     * Left object
     */
    public final L left;
    /**
     * Middle object
     */
    public final M middle;
    /**
     * Right object
     */
    public final R right;

    /**
     * <p>Obtains an immutable triple of from three objects inferring the generic types.</p>
     * <p>
     * <p>This factory allows the triple to be created using inference to
     * obtain the generic types.</p>
     *
     * @param <L>    the left element type
     * @param <M>    the middle element type
     * @param <R>    the right element type
     * @param left   the left element, may be null
     * @param middle the middle element, may be null
     * @param right  the right element, may be null
     * @return a triple formed from the three parameters, not null
     */
    @JsonCreator
    public static <L, M, R> ImmutableTriple<L, M, R> of(
            @JsonProperty("l") final L left,
            @JsonProperty("m") final M middle,
            @JsonProperty("r") final R right) {
        return new ImmutableTriple<>(left, middle, right);
    }

    /**
     * Create a new triple instance.
     *
     * @param left   the left value, may be null
     * @param middle the middle value, may be null
     * @param right  the right value, may be null
     */
    public ImmutableTriple(final L left, final M middle, final R right) {
        super();
        this.left = left;
        this.middle = middle;
        this.right = right;
    }
    //-----------------------------------------------------------------------

    /**
     * {@inheritDoc}
     */
    @Override
    @JsonProperty("l")
    public L getLeft() {
        return left;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    @JsonProperty("m")
    public M getMiddle() {
        return middle;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    @JsonProperty("r")
    public R getRight() {
        return right;
    }
}